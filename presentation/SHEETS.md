# GDO

GDO is a new approach to a framework.
It is under development as a hobby project since two decades.
It's main use case is rapid development of highly dynamic apps of middle size.

The current versions are [phpgdo](https://github.com/gizmore/phgpdo) (v7) and
[PyGDO](https:/github.com/gizmore/pygdo) (v8).

It is different to it's competitors, starting at the architecture.

GDO is MTTR not MVC, which is short for Model-Type-Type-Render,
emphasizing the central role of the types called GDT.

# Types

A framework usually comes with multiple different type systems, from different libraries.
The type system of the database differs from that in the html and Javascript or that in your HTTP routes.
If you are writing shell scripts for that framework there is probably another type system.

GDO has a single universal type system for everything.

A GDT knows how to behave in every context,
and your type definitions can be re-used in different spots of your application.

Due to the type hierarchy, we rarely need to write a custom validator,
and the types feature tooltips, icons and labels when used.

#
