from volosti_server_common.paths import get_static_path, get_templates_path


def test_static_path_getter() -> None:
    assert get_static_path().match('*/volosti_server_common/static')
    assert get_static_path().exists()


def test_templates_path_getter() -> None:
    assert get_templates_path().match('*/volosti_server_common/templates')
    assert get_templates_path().exists()
