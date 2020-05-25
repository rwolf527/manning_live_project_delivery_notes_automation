import os


def getfiles(root_dir=".", file_type=".pdf"):
    """finds all files of the specified type in the specified root_dir
       and all subdirectories.

    Keyword Arguments:
        root_dir {str} -- the starting directory to look in. (default: {'.'})
        file_type {str} -- the file extension to look for] (default: {'.pdf'})

    Returns:
        a python generator -- the fully qualified path for each file of the specified
        type in the specified directory and all subdirectories.
    """
    return (val for sublist in ((os.path.join(i[0], j) for j in i[2] if j.endswith(file_type))
                for i in os.walk(root_dir)) for val in sublist)


if __name__ == "__main__":
    for next_file in getfiles():
        print(next_file)
