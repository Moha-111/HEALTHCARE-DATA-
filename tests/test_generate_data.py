import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "src" / "generate_data.py"
MODULE_SPEC = importlib.util.spec_from_file_location("generate_data", MODULE_PATH)
generate_data = importlib.util.module_from_spec(MODULE_SPEC)
MODULE_SPEC.loader.exec_module(generate_data)


def test_generate_sample_data_creates_expected_base_columns():
    df = generate_data.generate_sample_data(num_records=5, expanded=False)

    assert len(df) == 5
    assert {
        'patient_id',
        'department',
        'visit_date',
        'wait_time_minutes',
        'los_minutes',
        'referral_delay_days',
        'age_group',
        'visit_outcome',
    }.issubset(df.columns)
    assert df['wait_time_minutes'].ge(5).all()
    assert df['los_minutes'].ge(30).all()
    assert df['referral_delay_days'].ge(0).all()
