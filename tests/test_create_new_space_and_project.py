from page_objects.base_page import BasePage


def test_create_new_space_and_project(driver, login):
    """Verify that a user can create a new space and project in Posit Cloud and the IDE is loaded."""
    # Create a new space and verify it is displayed in the space menu
    base_page = BasePage(driver)
    new_space_modal = base_page.create_new_space()
    new_space_modal.enter_space_name("test_new_space")
    new_space_modal.click_create_button()
    spaces = base_page.get_spaces()
    assert "test_new_space" in spaces

    # Create a new project and verify that the Posit Cloud IDE loads
    ide_page = base_page.create_new_rstudio_project()
    ide_page.switch_to_iframe()
    assert ide_page.is_console_visible()
    assert ide_page.is_workbench_files_visible()
    assert ide_page.is_workbench_environment_visible()
