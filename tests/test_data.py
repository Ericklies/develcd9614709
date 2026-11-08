from eda_predict_future_sales.config import FIGURES_DIR, PROJ_ROOT, RAW_DATA_DIR


def test_project_data_paths_are_inside_root():
    assert PROJ_ROOT.is_dir()
    assert RAW_DATA_DIR == PROJ_ROOT / "data" / "raw"
    assert FIGURES_DIR == PROJ_ROOT / "reports" / "figures"
