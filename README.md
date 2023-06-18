# tool-clear-image-of-deleted-products

## 安装
1. 解压压缩包
1. 确认系统装有python3环境，运行`python3 --version`显示python版本信息即为系统环境良好

## 使用方法
1. 准备好待删除的文件列表，即csv文件
1. 记下图片uploads目录位置，例如/home/example.com/wp-contents/uploads
1. 进入src目录
1. 运行程序: `python3 clear_image_of_deleted_products.py csv文件位置 uploads目录位置`
1. 如列出的文件不存在则会出现文字提示，如果文件存在则直接被删除，不会出现文字提示

## 更新日志
1. 添加了自动检测同目录下同产品图片功能，自动删除同目录下xxxx-*.xxx类似文件名图片，删除规则为文件名开头和扩展名与待删除文件相同，且在相同目录下