import pytest
from survey import AnonymousSurvey


@pytest.fixture
def my_survey():
    """创建一个AnonymousSurvey实例作为测试夹具。

    Returns:
        AnonymousSurvey: 包含预设问题的匿名调查对象
    """
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)
    return my_survey


def test_store_single_response(my_survey):
    """测试存储单个回答的功能。

    Args:
        my_survey (AnonymousSurvey): 通过fixture提供的调查对象
    """
    # 存储一个回答并验证它是否正确添加到响应列表中
    my_survey.store_response("English")
    assert "English" in my_survey.responses


def test_store_three_responses(my_survey):
    """测试存储三个回答的功能。

    Args:
        my_survey (AnonymousSurvey): 通过fixture提供的调查对象
    """
    # 准备三个测试回答
    responses = ["English", "Spanish", "Mandarin"]

    # 依次存储所有回答
    for response in responses:
        my_survey.store_response(response)

    # 验证所有回答都已正确存储
    for response in responses:
        assert response in my_survey.responses
