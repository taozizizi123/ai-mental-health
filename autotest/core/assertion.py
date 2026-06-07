def assert_code(res, expect_code=200):
    """断言http状态码"""
    assert res is not None, "响应为空"
    assert res.status_code == expect_code, f"实际码{res.status_code}≠预期{expect_code}"

def assert_json_key(res, key):
    """断言返回json包含key字段"""
    assert res is not None, "响应为空"
    json_data = res.json()
    # 检查 data 中是否有该 key，或者根节点有该 key
    if "data" in json_data:
        assert key in json_data["data"] or key in json_data, f"返回数据无{key}字段"
    else:
        assert key in json_data, f"返回数据无{key}字段"

def assert_json_value(res, key, value):
    """断言key对应值等于value"""
    assert res is not None, "响应为空"
    json_data = res.json()
    # 优先从 data 中找
    if "data" in json_data:
        assert json_data["data"].get(key) == value or json_data.get(key) == value, f"{key}实际值{json_data.get(key)}≠{value}"
    else:
        assert json_data.get(key) == value, f"{key}实际值{json_data.get(key)}≠{value}"

def assert_business_success(res):
    """断言业务成功（code 为 200 或 "200"）"""
    assert res is not None, "响应为空"
    json_data = res.json()
    code = json_data.get("code")
    assert code in [200, "200"], f"业务失败，code={code}"