import sys
import os
from shutil import copyfile

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " project_name")

project_name = sys.argv[1]

project_path = project_name + "/" + project_name

os.mkdir(project_name, 0755)
os.mkdir(project_path, 0755)
os.mkdir(project_path + "/src", 0755)
os.mkdir(project_path + "/tools", 0755)
os.mkdir(project_path + "/3rd", 0755)
os.mkdir(project_name + "/vs", 0755)

build_file = project_path + "/build.sh"
copyfile("build.sh", build_file)

demo_file = project_path + "/src/" + project_name + ".cpp"
copyfile("demo.cpp", demo_file)

cmake_dst_path = project_path + "/CMakeLists.txt"
cmake_src = open("CMakeLists.txt")
cmake_dst = open(cmake_dst_path, "w")
cmake_dst.write("set(PROJECT_NAME " + project_name + ")\n")
for line in cmake_src:
    cmake_dst.write(line)
cmake_src.close()
cmake_dst.close()
