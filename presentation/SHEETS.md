# GDO

GDO is a new approach to a framework.
It is under development as a hobby project since two decades.
It's main use case is rapid development of highly dynamic apps of middle size.

The current versions are [phpgdo](https://github.com/gizmore/phgpdo) (v7) and
[PyGDO](https:/github.com/gizmore/pygdo) (v8).

It is different to its competitors, starting at the architecture.

GDO is MTTR not MVC, which is short for Model-Type-Type-Render,
emphasizing the central role of the types called GDT.

# Types

A framework usually comes with multiple different type systems, from different libraries.
The type system of the database differs from that in the HTML and JavaScript or that in your HTTP routes.
If you are writing shell scripts for that framework there is probably another type system.

GDO has a single universal type system for everything.

A GDT knows how to behave in every context,
and your type definitions can be re-used in different spots of your application.

Due to the type hierarchy, we rarely need to write a custom validator.
The types feature also tooltips, icons and labels when used.

# Connect

If you are writing a cool application, you probably want more than HTTP.
PyGDO is written as a kraken, everything knows anything.

In old terms, we have great Inter-Process-Communication,
using REDIS as the one and only memory, and as a major cache.

We support any text based system, like Slack, Discord, Telegram, HTTP, bash, TCP/IP, and more.
Our Programming language is english now – or any other supported one.

# Amazing

I do not know if you ever were surprised how good your own software and ideas turn out.
With PyGDO, I do experience that on a daily basis.
