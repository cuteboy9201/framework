<!--
 * @Author: YouShumin
 * @Date: 2020-09-17 14:59:42
 * @LastEditTime: 2020-09-17 17:02:30
 * @LastEditors: YouShumin
 * @Description: Another flat day
 * @FilePath: /KwGameManager/api.md
-->
## 通用数据结构
* 返回数据 json
    * code: int类型, 必须, 0代表成功
    * data: object类型,非必须, 用于返回具体的数据
    * msg: string类型, 返回信息说明,成功="success", 失败="error内容"  

    ```
    {
        "code": 0, 
        "data": {
                ...
            },
        "msg": "success"
    }
* 常用接口
    * read: 读取单条数据 GET 
        * 参数 id, 唯一字段ID; resId 资源ID(可选)
        * 示例 /get?id=123&resId=demo
        * 返回数据
        
        ```
        {
            "code": 0,
            "data": {
                "testName": "123",
                "testDate": 12345678,
                "id": 123,
            },
            "msg": "success"
        }
        ```
    
    * update: 更新单条数据 PUT
        * 参数 id,唯一字段ID; resId 资源ID(可选)
        * 示例 /update?id=123&resId=demo
        * 返回结构
        ```
        {
            "code": 0,
            "data": {
                "testName": "123",
                "testDate": 12345678
            },
            "msg": "success"
        }
        ```

    * create: 创建单条数据 POST
        * 参数 resId 资源ID(可选)
        * 示例 /create?resId=demo `data: {"testname":123, "password":"123"}`
        * 返回结构
        ```
        {
            "code": 0,
            "data": {
                "testName": "123",
                "testDate": 12345678
            },
            "msg": "success"
        }

        ```
    
    * delete: 删除单条数据 DELETE
        * 参数 id唯一字段ID, resId 资源ID(可选)
        * 示例 /delete?id=123&resId=demo
        * 返回结构
        ```
        {
            "code": 0,
            "data": {},
            "msg": "success"
        }
        ```        
    
    * list: 列表数据接口 GET
        * 参数
            * resId 资源ID
            * 搜索/筛选 key=value 
            * sortField 排序字段
            * sortOrder asc|desc 升序|降序
            * page 分页默认为1
            * size 分页条母 默认为10
        * 示例 /list?resId=demo&size=10&sortField=lastTime&sortOrder=desc&status=1&tags=标签

        * 返回结构
        ```
        {
            "code": 0, d
            "data": {
                "list": [ // 凡是涉及到列表类型到数据，都使用 list 这个字段以数组类型返回
                    {
                        "testName": "123",
                        "testDate": 12345678
                    },
                    {
                        "testName": "123",
                        "testDate": 12345678
                    }
                ],
                "total": 992 // 凡是需要分页的，都需要返回 total 这个字段。相反，如果不想显示分页，接口不反回这个字段即可
            },
            "msg": "success"
        }
        ```