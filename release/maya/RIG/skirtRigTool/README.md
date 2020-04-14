# -copyright@2019

# 拖拽install.mel到maya界面中。或者使用下面脚本进行部署

    import sys
    inpath = r'../skirtRigTool'
    inpath in sys.path or sys.path.append(inpath )
    from scripts import skirtRig
    skirtRig.show()

# 注意事项
    maya中需要有PyQt5.下载路径https://github.com/MChenLiang/mayaPyQt5.git
    
# 2020.04.05
    插件UI修改为PyQt5。
    # 新增功能
        修正骨骼的轴向
        控制器支持缩放
        方向预览
        控制器生成方向在界面中的显示
    .

# 2020.01.10
    新增末端控制器功能。勾选endEffector，将会生成末端控制器.
