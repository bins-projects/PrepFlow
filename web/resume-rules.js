(function () {
  function resumeDescription(saved) {
    const questionCount = Array.isArray(saved.sessionQuestions)
      ? saved.sessionQuestions.length
      : 0;

    const blockSize = Number(saved.sessionBlockSize) || 15;
    const totalBlocks = Math.max(1, Math.ceil(questionCount / blockSize));
    const currentBlock = Math.min(
      Math.max(Number(saved.blockNumber) || 1, 1),
      totalBlocks
    );

    return `Block ${currentBlock} of ${totalBlocks}`;
  }

  function resumeAriaLabel(description) {
    return `Continue session: ${description}`;
  }

  window.PrepFlowResumeRules = {
    resumeDescription,
    resumeAriaLabel,
  };
}());
