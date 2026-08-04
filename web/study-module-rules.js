(function (global) {
  "use strict";

  const SUPPORTED_FORMAT = "prepflow_module_selection";
  const SUPPORTED_VERSION = "1.0";

  function requireValue(condition, message) {
    if (!condition) {
      throw new Error(`Invalid study module: ${message}`);
    }
  }

  function validateManifest(manifest) {
    requireValue(manifest && typeof manifest === "object", "manifest must be an object");
    requireValue(manifest.format === SUPPORTED_FORMAT, `unsupported format ${manifest.format}`);
    requireValue(manifest.version === SUPPORTED_VERSION, `unsupported version ${manifest.version}`);
    requireValue(typeof manifest.module_id === "string" && manifest.module_id, "module_id is required");
    requireValue(typeof manifest.title === "string" && manifest.title, "title is required");
    requireValue(Array.isArray(manifest.groups) && manifest.groups.length > 0, "groups are required");
    requireValue(manifest.behavior?.navigation === "subject_then_chapter", "subject-then-chapter navigation is required");
    requireValue(manifest.behavior?.delivery === "one_question_at_a_time", "one-question delivery is required");
    requireValue(manifest.behavior?.scoring === "first_attempt_by_chapter", "chapter scoring is required");
    requireValue(manifest.behavior?.shuffle === "once_per_chapter", "chapter shuffle is required");
    requireValue(manifest.behavior?.reuse_existing_quiz_engine === true, "existing quiz engine reuse is required");

    const references = new Set();
    let chapterCount = 0;
    let questionCount = 0;

    manifest.groups.forEach((group) => {
      requireValue(typeof group.subject === "string" && group.subject, "group subject is required");
      requireValue(typeof group.source_pack_id === "string" && group.source_pack_id, "source_pack_id is required");
      requireValue(Array.isArray(group.chapters) && group.chapters.length > 0, `${group.subject} has no chapters`);

      group.chapters.forEach((chapter) => {
        requireValue(Number.isInteger(chapter.source_chapter), `${group.subject} chapter number is invalid`);
        requireValue(typeof chapter.title === "string" && chapter.title, `${group.subject} chapter title is required`);
        requireValue(Array.isArray(chapter.question_ids) && chapter.question_ids.length > 0, `${chapter.title} has no questions`);
        requireValue(chapter.question_ids.length === chapter.expected_question_count, `${chapter.title} expected count does not match its IDs`);
        chapterCount += 1;
        questionCount += chapter.question_ids.length;

        chapter.question_ids.forEach((questionId) => {
          requireValue(typeof questionId === "string" && questionId, `${chapter.title} contains an invalid question ID`);
          requireValue(!references.has(questionId), `duplicate question reference ${questionId}`);
          references.add(questionId);
        });
      });
    });

    requireValue(questionCount === manifest.expected_question_count, "expected total does not match question references");
    return { chapterCount, questionCount };
  }

  function resolveChapter(group, chapter, pack, packPath) {
    requireValue(pack && pack.pack_id === group.source_pack_id, `Pack ${group.source_pack_id} could not be loaded`);
    const byId = new Map();
    pack.questions.forEach((question) => {
      requireValue(!byId.has(question.id), `canonical Pack contains duplicate ID ${question.id}`);
      byId.set(question.id, question);
    });

    return chapter.question_ids.map((questionId) => {
      const question = byId.get(questionId);
      requireValue(question, `missing question reference ${questionId}`);
      requireValue(question.chapter === chapter.source_chapter, `${questionId} does not belong to chapter ${chapter.source_chapter}`);
      requireValue(question.chapter_title === chapter.title, `${questionId} chapter title does not match the manifest`);
      return { packPath, questionId };
    });
  }

  global.PrepFlowStudyModuleRules = { validateManifest, resolveChapter };
})(window);
