from product import simple_product

def test_simple_product():
    cases = [
                [1, 2, 3, 4, 5],
                [3, 2, 1]
            ]
    expected_results = [
                [120, 60, 40, 30, 24],
                [2, 3, 6]
             ]
    for case, expect_result in zip(cases, expected_results):
        assert simple_product(case) == expect_result
