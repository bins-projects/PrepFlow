(function () {
  function nextQuestionStep(questionIndex, blockEnd) {
    const nextQuestionIndex = questionIndex + 1;

    return {
      questionIndex: nextQuestionIndex,
      blockComplete: nextQuestionIndex >= blockEnd,
    };
  }

  function completedFirstPassStep(missedCount, hasMoreQuestions) {
    if (Math.max(0, Number(missedCount) || 0) > 0) {
      return "review";
    }

    return hasMoreQuestions ? "next-block" : "final-summary";
  }

  function completedReviewStep(hasMoreQuestions) {
    return hasMoreQuestions ? "next-block" : "final-summary";
  }

  window.PrepFlowNavigationRules = {
    nextQuestionStep,
    completedFirstPassStep,
    completedReviewStep,
  };
}());
