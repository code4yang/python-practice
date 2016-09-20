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
        includes.append(buildxml(path, type))

    return includes


def buildxml(path, type):
    ret = ''
    if type == 'html':
        ret = '<include name="' + path[path.find('html/') + 4:] + '" />\r\n'
    elif type == 'config':
        ret = '<include name="WEB-INF/classes' + path[path.find('config/') + 6:] + '" />\r\n'
    elif type == 'class':
        ret = '<include name="WEB-INF/classes' + path[path.find('src/') + 3:][:-4] + 'class" />\r\n'
    return ret


if __name__ == '__main__':
    rtnset = read_changelog('changeLog.txt')
    rtnList = set_type(rtnset)
    xml = open('build1.xml', mode='wt')
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
    xml.writelines('''
</fileset>
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
