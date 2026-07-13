# <span>Filters</span> <span>Property</span>



**Applies To:** [FileBox](../objects/filebox.md)

**Description**


The Filters property is a nested scalar or vector containing a list of filters. Each filter is a 2-element vector of character vectors which contain a file type mask and a file type description respectively. The file type descriptions appear in a drop-down combo box labelled "List Files of Type". When the user selects one of these, the currently selected directory is searched for files which match the corresponding mask. The default value of Filters is an empty vector. This gives a file type mask of "*.*" and a file type description of "All Files (*.*)". Hence an empty vector is equivalent to `(⊂'*.*' 'All Files (*.*)')`.



