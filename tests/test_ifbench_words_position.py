from lm_eval.tasks.ifbench import instructions, instructions_util


def test_words_position_checker_handles_two_tokens_plus_punctuation(monkeypatch):
    checker = instructions.WordsPositionChecker("words:words_position")
    checker.build_description(keyword="alpha")

    # This tokenization shape used to crash due to words[-3] indexing.
    monkeypatch.setattr(
        instructions_util.nltk,
        "word_tokenize",
        lambda _: ["alpha", "."],
    )

    assert checker.check_following("alpha.") is False


def test_words_position_checker_keeps_two_word_case_valid(monkeypatch):
    checker = instructions.WordsPositionChecker("words:words_position")
    checker.build_description(keyword="alpha")

    # Two words can still satisfy: second word == second-to-last word == keyword.
    monkeypatch.setattr(
        instructions_util.nltk,
        "word_tokenize",
        lambda _: ["alpha", "alpha"],
    )

    assert checker.check_following("alpha alpha") is True
