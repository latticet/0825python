"""
读取文件内容
写入内容到文件中
复制文件
删除文件
文件改名
"""
import os


class File:
    def read(self, filename):
        """读取文件内容"""
        f = open(filename, 'r', encoding='utf8')
        content = f.read()
        f.close()
        return content

    def append(self, filename, content):
        """写入内容到文件中"""
        f = open(filename, 'a', encoding='utf8')
        f.write(content)
        f.close()

    def copy(self, filename):
        """复制文件"""
        # 装备目标文件名称  demo.txt -> demo本-副.txt
        source_filename, extension = os.path.splitext(filename)  # (文件名, 后缀)
        target_filename = source_filename + '-副本' + extension

        # 打开源文件和目标文件
        source_file = open(filename, 'rb')
        target_file = open(target_filename, 'wb')

        # 开始写入
        while True:
            content = source_file.read(1024)
            if not content:
                break
            target_file.write(content)

        # 关闭资源
        source_file.close()
        target_file.close()

    def del_file(self, filename):
        """删除文件"""
        os.remove(filename)

    def rename(self, filename, new_filename):
        """文件改名"""
        os.rename(filename, new_filename)


if __name__ == '__main__':
    file = File()
    # 写入内容到文件中
    file.append('demo.txt', '123\n456\n789')
    # 读取文件内容
    print(file.read('demo.txt'))
    # 复制文件
    file.copy('demo.txt')
    # 删除文件
    file.del_file('demo-副本.txt')
    # 文件改名
    file.rename('demo.txt', 'mydemo.txt')
