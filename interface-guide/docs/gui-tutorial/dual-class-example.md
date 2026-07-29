# Dual Class Example

The Dual Class example is based upon the example used to illustrate how you may build an ActiveX Control in Dyalog APL (see [The Dual Control Tutorial](../activex-control/dual-control-tutorial.md)), but re-engineered as an internal Dyalog APL Class. The full listing of the Dual Class script is provided overleaf.

This version of Dual is based upon a SubForm:
```apl
      :Class Dual: 'SubForm'
```

The Dual Control requires a GUI parent but several Instances can co-exist, quite independently, in the same parent.

For example, function `RUN` creates a Form and 3 Instances of Dual; one to convert Centigrade to Fahrenheit, one to convert Fahrenheit to Centigrade, and the third to convert centimetres to inches.
```apl
     ∇ RUN;F;D1PROPS;D2PROPS;D3PROPS
[1]
[2]    F←⎕NEW'Form'(('Caption' 'Dual Instances')
                    ('Coord' 'Pixel')('Size'(320 320)))
[3]
[4]    D1PROPS←('Caption1' 'Centigrade')
               ('Caption2' 'Fahrenheit')
[5]    D1PROPS,←('Intercept' 32)('Gradient'(9÷5))
                ('Value1' 0)('Range'(0 100))
[6]    F.D1←F.⎕NEW Dual(('Coord' 'Pixel')('Posn'(10 10))
                        ('Size'(100 300)),D1PROPS)
[7]
[8]    D2PROPS←('Caption1' 'Fahrenheit')
               ('Caption2' 'Centigrade')
[9]    D2PROPS,←('Intercept'(-32×5÷9))('Gradient'(5÷9))
                ('Value1' 0)('Range'(0 212))
[10]   F.D2←F.⎕NEW Dual(('Coord' 'Pixel')('Posn'(110 10))
                        ('Size'(100 300)),D2PROPS)
[11]
[12]   D3PROPS←('Caption1' 'Centimetres')
               ('Caption2' 'Inches')
[13]   D3PROPS,←('Intercept' 0)('Gradient'(÷2.54))
                ('Value1' 0)('Range'(0 100))
[14]   F.D3←F.⎕NEW Dual(('Coord' 'Pixel')('Posn'(210 10))
                        ('Size'(100 300)),D3PROPS)
[15]
[16]   ⎕DQ'F'
     ∇
```

![](../img/dual-instances.png)

Dual's Constructor `Make` first splits its constructor arguments into those that apply to the Dual Class itself, and those that apply to the SubForm. Its `:Implements Constructor` statement then passes these on to the Base Constructor, together with an appropriate setting for EdgeStyle.
```apl
     :Implements Constructor :Base BaseArgs,
                                   ⊂'EdgeStyle' 'Dialog'
```

## Dual Class Example
```apl
:Class Dual: 'SubForm'
    :Include GUITools
    :Field Private _Caption1←''
    :Field Private _Caption2←''
    :Field Private _Value1←0
    :Field Private _Value2←0
    :Field Private _Range←0
    :Field Private _Intercept←0
    :Field Private _Gradient←1
    :Field Private _Height←40
    
```
```apl

    ∇ Create args;H;W;POS;SH;CH;Y1;Y2;BaseArgs;MyArgs;
                  Defaults
      :Access Public
      MyArgs BaseArgs←SplitNV args
      :Implements Constructor :Base BaseArgs,
                                    ⊂'EdgeStyle' 'Dialog'
      ExecNV_ MyArgs ⍝ Set Flds named _PropertyName 
                                      MyArgs
      Coord←'Pixel'
      H W←Size
      POS←2↑⌊0.5×0⌈(H-_Height)
      CH←⊃GetTextSize'W'
      'Slider'⎕WC'TrackBar'POS('Size'_Height W)
      Slider.(Limits AutoConf)←_Range 0
      Slider.(TickSpacing TickAlign)←10 'Top'
      Slider.onThumbDrag←'ChangeValue'
      Slider.onScroll←'ChangeValue'
      Y1←POS[1]-CH+1
      Y2←POS[1]+_Height+1
      'Caption1_'⎕WC'Text'_Caption1(Y1,0)('AutoConf' 0)
      'Caption2_'⎕WC'Text'_Caption2(Y2,0)('AutoConf' 0)
      'Value1_'⎕WC'Text'(⍕_Value1)(Y1,W)('HAlign' 2)
                        ('AutoConf' 0)
      CalcValue2
      'Value2_'⎕WC'Text'(⍕_Value2)(Y2,W)('HAlign' 2)
              ('AutoConf' 0)
      onConfigure←'Configure'
    ∇
    
    :Property Caption1, Caption2
    :Access Public
        ∇ R←Get arg
          R←(arg.Name,'_')⎕WG'Text'
        ∇
        ∇ Set arg
          (arg.Name,'_')⎕WS'Text'arg.NewValue
        ∇
    :EndProperty
    
    
    :Property Value1
    :Access Public
        ∇ R←Get
          R←_Value1
        ∇
        ∇ Set arg
          ⎕NQ'Slider' 'Scroll' 0 arg.NewValue
        ∇
    :EndProperty
    
```
```apl

    :Property Intercept, Gradient, Range, Height, Value2
    :Access Public
        ∇ R←Get arg
          R←⍎'_',arg.Name
        ∇
    :EndProperty
    
    ∇ CalcValue2
      _Value2←_Intercept+_Gradient×_Value1
    ∇
    
    ∇ ChangeValue MSG
      ⍝ Callback for ThumbDrag and Scroll     
      _Value1←⊃¯1↑MSG
      CalcValue2
      Value1_.Text←⍕_Value1
      Value2_.Text←⍕_Value2
    ∇
    
    ∇ Configure MSG;H;W;POS;CH;Y1;Y2
      2 ⎕NQ MSG
      H W←Size
      POS←2↑⌊0.5×(H-_Height)
      CH←⊃GetTextSize'W'
      Slider.(Posn Size)←POS(_Height W)
      Y1←POS[1]-CH+1
      Y2←POS[1]+_Height+1
      Caption1_.Points←1 2⍴Y1,0
      Caption2_.Points←1 2⍴Y2,0
      Value1_.Points←1 2⍴Y1,W
      Value1_.Points←1 2⍴Y2,W
    ∇
    
:EndClass ⍝ Dual
```

The utilities contained in in the GUITools Namespace are as follows:
```apl
     ∇ r←SplitNV args;m
[1]   ⍝ Parse Name,Value Pairs
[2]   ⍝ Return pairs for this class in 1st element,
        others in 2nd element
[3]    m←(⎕NC⊃¨args)∊2.2 2.3 ⍝ Fields/Properties
                               in derived class
[4]    r←(m/args)((~m)/args)
     ∇
      ∇ExecNV_∇
     ∇ r←ExecNV_ args;n;v
[1]   ⍝ Set Properties using Name,Value Pairs
[2]    n v←↓⍉↑args
[3]    n←'_',¨n
[4]    ⍎(⍕,n,⊂'n'),'←v,0'
     ∇
```
