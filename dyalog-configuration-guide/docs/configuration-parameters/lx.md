# LX

!!! Info "Information"
    This configuration parameter is only relevant when using the Unicode edition of Dyalog, and only in the development interpreter (it is ignored in run-time applications).

An expression to be executed after Dyalog has started and loaded a workspace or a text file of APL source code (see [`Load`](load.md)). It is run only at start-up and overrides the workspace latent expression `⎕LX`; it is ignored when a workspace is loaded other than at start-up.

Valid values are an APL expression.

Related parameters: [Load](load.md).
