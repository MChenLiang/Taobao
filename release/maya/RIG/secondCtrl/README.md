# -copyright@2020

## 拖拽install.mel到maya界面中。或者使用下面脚本进行部署

    import sys
    inpath = r'../secondCtrl'
    inpath in sys.path or sys.path.append(inpath )
    from scripts import openUI
    openUI.encryption()

## 注意事项
    maya中需要有PyQt5.下载路径https://github.com/MChenLiang/mayaPyQt5.git
    
## 2020.04.02
    第一版正式发布

