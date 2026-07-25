(function () {
  function chooseSummaryAction({ mastered, missedCount, hasMoreQuestions }) {
    if (!mastered && missedCount > 0) {
      return {
        action: "review",
        label: "Review Missed Questions",
      };
    }

    if (hasMoreQuestions) {
      return {
        action: "next-block",
        label: "Start Next Block",
      };
    }

    return {
      action: "finish",
      label: "Finish Session",
    };
  }

  function blockSummaryAction({ mastered, missedCount, blockEnd, totalQuestions }) {
    return chooseSummaryAction({
      mastered,
      missedCount,
      hasMoreQuestions: blockEnd < totalQuestions,
    });
  }

  function summaryAction({ mastered, missedCount, hasMoreQuestions }) {
    return chooseSummaryAction({
      mastered,
      missedCount,
      hasMoreQuestions: Boolean(hasMoreQuestions),
    });
  }

  window.PrepFlowSummaryRules = {
    blockSummaryAction,
    summaryAction,
  };
}());
