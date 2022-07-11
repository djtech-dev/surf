COMPILERS = {
    ".rs"
    ".go"
    ".zig"
    ".cbl"
    ".cob"
    ".f"
    ".for"
    ".f90"
    ".f95"
    ".jakt"
    ".adb"
    ".ads"
    ".d"
    ".m"
    ".mm"
    ".swift"
    ".v"
    ".hx"
    ".hs"
    ".pp"
    ".pas"
    ".nim"
    ".nims"
    ".cr"
}
GCC = {
    ".c": "gcc {ext_args} -o {output_file} {file_path}",
    ".cpp": "gcc {ext_args} -o {output_file} {file_path} -lstdc++",
}
LLVM = {
    ".c": "clang {ext_args} -o {output_file} {file_path}",
    ".cpp": "clang {ext_args} -o {output_file} {file_path}",
    ".m": "clang -ObjC {ext_args} -o {output_file} {file_path}",
    ".mm": "clang -ObjC++ {ext_args} -o {output_file} {file_path}",
}