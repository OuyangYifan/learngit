import yaml
"""Basic Rules of yaml
 1. 大小写敏感
 2. 使用缩进表示层级关系
 3. 缩进时不允许使用Tab，只允许使用空格
 4. 缩进的空格数目不重要，只要相同层级的元素左对齐即可
 5. # 表示注释，从它开始到行尾都被忽略
"""
f = open(r"D:\SandBox_Dev\Git\dev\learngit\Yaml_dat\Conf_v0.yml")
y = yaml.load(f)
print(y)

#load_all returns a iterator of all contents parsed from yaml file
print("Parsing and accessing the file content by iterator")
f = open(r"D:\SandBox_Dev\Git\dev\learngit\Yaml_dat\Conf_v0.yml")
z = yaml.load_all(f)
for data in z:
    print(data)
