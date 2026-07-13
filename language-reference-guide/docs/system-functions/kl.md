---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕KL KL
</div>

# <span>Key Label</span> `R←⎕KL Y`{{key}}

`Y` is a simple character vector or a vector of character vectors containing Input Codes for Keyboard Shortcuts. In the Classic Edition, keystrokes are associated with Keyboard Shortcuts by the Input Translate Table.

`R` is a simple character vector or a vector of character vectors containing the labels associated with the codes.  If `Y` specifies codes that are not defined, the corresponding elements of `R` are the codes in `Y`.

`⎕KL` provides the information required to build device-independent help messages into applications, particularly full-screen applications using `⎕SM` and `⎕SR`.

<h2 class="example">Examples</h2>
```apl
      ⎕KL 'RC'
Right
 
      ⎕KL 'ER' 'EP' 'QT' 'F1' 'F13'
  Enter  Esc  Shift+Esc  F1  Shift+F1
```

!!! windows "Dyalog on Microsoft Windows"
    In the Unicode edition, `⎕KL` can also get the keystrokes to type APL glyphs:
    ```apl
          ⎕KL '⌸'
    Control+Shift+K
    ```
