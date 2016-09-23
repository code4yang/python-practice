"""
 修改changelog为特定格式
"""
import re

htmlextends = ['html', 'page', 'uientity', 'application']
clazzextends = ['java']
configextends = ['bo', 'svpkg', 'cmpt']


def read_changelog(filename):
    file = open(filename, mode='r', encoding='utf-8')
    lines = file.readlines()
    reg = re.compile(r'\W*[AM]\W*(/.*\.\w*)$')
    sets = set()
    for line in lines:
        result = reg.match(line)
        if result is not None:
            sets.add(result.group(1))
    return sets


def set_type(sets):
    includes = []
    for path in sets:
        extends = path[path.rfind('.') + 1:]
        type = ''
        if extends in htmlextends:
            type = 'html'
        elif extends in clazzextends:
            type = 'class'
        elif extends in configextends:
            type = 'config'
        else:
            raise NameError('未知拓展名')
        includes.append(buildxml(path, type))

    return includes


def buildxml(path, type):
    ret = ''
    if type == 'html':
        ret = '<include name="' + path[path.find('html/') + 5:] + '" />\n'
    elif type == 'config':
        ret = '<include name="WEB-INF/classes' + path[path.find('config/') + 6:] + '" />\n'
    elif type == 'class':
        ret = '<include name="WEB-INF/classes' + path[path.find('src/') + 3:][:-4] + 'class" />\n'
    return '\t\t\t\t\t'+ret


if __name__ == '__main__':
    print('----->开始读取changeLog。txt')
    rtnset = read_changelog('changeLog.txt')
    print('----->读取changeLog。txt完成')
    print('----->开始对内容分类处理')
    rtnList = set_type(rtnset)
    print('----->处理完成')
    print('----->开始写入build.xml文件')
    xml = open('build.xml', mode='wt', encoding='utf-8')
    xml.writelines('''<?xml version="1.0" encoding="utf-8"?>
    <project name="rms deploy" default="antwar" basedir=".">
        <property file="build.properties" />
        <target name="antwar" description="打包war" depends="">
            <echo message="删除原dist目录下的${war.present}"/>
            <delete file="${project.dist.dir}/${war.present}" />
            <echo message="拷贝HTML文件..." />
            <copy todir="${project.temp.dir}">
                <fileset dir="${webroot.path}">
''')
    xml.writelines(rtnList)
    xml.writelines('''                </fileset>
            </copy>
        <echo message="生成${war.present}..." />
        <war warfile="${project.dist.dir}/${war.present}.war" webxml="${project.temp.dir}/WEB-INF/web.xml">
            <fileset dir="${project.temp.dir}">
                <include name="**/*"/>
                <exclude name="**/svn/**"/>
                <exclude name="**/_apx/**"/>
            </fileset>
        </war>
    </target>
</project>
    ''')
    print('----->写入build.xml文件完成')
