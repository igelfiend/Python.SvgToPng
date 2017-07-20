import os
import sys


def main():
    files = sys.argv[1:]
    for dname in files:
        dir_name = dname
        current_dir = os.getcwd()

        if os.path.basename(current_dir) == "devices":
            target_dir = current_dir + "/../devices_png/" + dir_name
        else:
            target_dir = current_dir + "/" + dir_name + "_png"

        src_dir = current_dir + "/" + dir_name
        print("src: " + src_dir)
        print("trg: " + target_dir)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        svg_to_png(src_dir, target_dir)


def svg_to_png( src_path, target_path ):
    for f in os.listdir(src_path):
        if os.path.isdir(src_path + "/" + f):
            new_target_path = target_path + "/" + f
            new_src_path = src_path + "/" + f
            print("make: " + new_target_path)

            if not os.path.exists(new_target_path):
                os.makedirs(new_target_path)

            print("path: " + new_src_path)
            svg_to_png( new_src_path, new_target_path )

        # if f.endswith(".svg"):
        #     print("run: magick " + src_path + "/" + f + " " + target_path + "/" + f[0:-3] + "png")
        #     os.system("magick " + src_path + "/" + f + " " + target_path + "/" + f[0:-3] + "png")

        if f.endswith(".svg"):
            print("inkscape " + src_path + "/" + f + " --export-png=" + target_path + "/" + f[0:-3] + "png")
            os.system("inkscape " + src_path + "/" + f + " --export-png=" + target_path + "/" + f[0:-3] + "png")


if __name__ == "__main__":
    main()
