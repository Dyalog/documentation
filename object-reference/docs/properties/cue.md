# <span>Cue</span> <span>Property</span>

**Applies To:** [ButtonEdit](../objects/buttonedit.md), [Edit](../objects/edit.md)

**Description**

This  property specifies optional text to be displayed when a [ButtonEdit](../objects/buttonedit.md) or an [Edit](../objects/edit.md) object is empty. For an [Edit](../objects/edit.md) object it applies only if the Style of the [Edit](../objects/edit.md) object is `'Single'`.

!!! note
    This feature only applies if [Native Look and Feel](../miscellaneous/windows-xp-look-and-feel.md) is enabled.

The Boolean property [ShowCueWhenFocused](showcuewhenfocused.md)  determines whether or not the cue should also be displayed once the user has tabbed into or clicked on the input field (and thus given it the focus).

<h2 class="example">Example</h2>
```apl

      'F' ⎕WC 'Form' 'Cue Property'
      'F.E' ⎕WC 'Edit'
       F.E.Cue←'Enter Password'
```

![](../img/cue-property.png)
