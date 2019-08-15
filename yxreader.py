import os

from app import create_app

if __name__ == '__main__':
    app = create_app()
    # 解决 debug 模式下 启动两次的问题
    # 详见：https://www.kancloud.cn/hx78/python/450124
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        print('well done, good job ')
    app.run(debug=True, host='0.0.0.0', port=5001)
