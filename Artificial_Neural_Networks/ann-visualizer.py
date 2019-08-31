# pip install ann_visualizer
# pip install graphviz


from ann_visualizer.visualize import ann_viz;

ann_viz(classifier, title="My first neural network")


# if get error like below on mac
"""
ExecutableNotFound: failed to execute ['dot', '-Tpdf', '-O', 
'network.gv'], make sure the Graphviz executables 
are on your systems' PATH
"""
# for mac 
#  brew install graphviz


"""

For Windows:

Install windows package from: https://graphviz.gitlab.io/_pages/Download/Download_windows.html
Install python graphviz package
Add C:\Program Files (x86)\Graphviz2.38\bin to User path
Add C:\Program Files (x86)\Graphviz2.38\bin\dot.exe to System Path

"""
