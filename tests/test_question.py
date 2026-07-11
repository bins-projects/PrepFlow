from study.question import check_answer


def test_multiple_response_accepts_answers_in_any_order():
    assert check_answer("CBA", ["A", "B", "C"])


def test_ordered_response_rejects_wrong_order():
    assert not check_answer("BAC", ["A", "B", "C"], "ordered_response")
