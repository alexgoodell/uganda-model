# uganda-model
modeling supply of anesthesia providers in uganda

- note: binder currently not working due to too many dependencies!
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/alexgoodell/uganda-model/master?filepath=model%2Fpy%2Fuganda-model.ipynb)

## Project data flow
![structure](http://interactive.blockdiag.com/image?compression=deflate&encoding=base64&src=eJyFjFsKwkAMRf-7imzAFYhuRdKZtIaOk5BJlSLu3RmRClXwJ49zuLdPEqbIOMK9AxBjyo7OkuEAKuaG7PuuqgEDJ3amArsj6HkpHBhz-VJZsbI623MTmwaxQBV9Mluz3k1c0Rj7RGUrLqjKeaz4fTUos-vsp8hGwcWWv3atf1VKpNQibf8MPJ6Lq2L_)

[Edit this diagram](http://interactive.blockdiag.com/?compression=deflate&src=eJyFjFsKwkAMRf-7imzAFYhuRdKZtIaOk5BJlSLu3RmRClXwJ49zuLdPEqbIOMK9AxBjyo7OkuEAKuaG7PuuqgEDJ3amArsj6HkpHBhz-VJZsbI623MTmwaxQBV9Mluz3k1c0Rj7RGUrLqjKeaz4fTUos-vsp8hGwcWWv3atf1VKpNQibf8MPJ6Lq2L_)


![data structure](misc/data-flow.svg)

[Edit this diagram](https://mermaidjs.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcbmRzW2Rpc3RyaWN0c10gLS0-IGZjXG5iZ1tCdWRnZXQgb2ZmaWNlIGRpc3RyaWN0IGRhdGEsIG90aW1zXzIwMThdIC0tPiBkc1xudW1bVU1EUEMgcmVnaXN0cnksIHVtZHBjMjAxOF0gLS0-IG1kW2FkZl0gXG5tZCAtLT4gIG1kYWRmW21kYV9kZl1cbm5wYSAtLT4gbnBhZGZbbnBhX2RmXVxuZm1bRmFjaWxpdHkgbWFzdGVyIGxpc3QsIG1vaGRoaTIwMTddIC0tPiBmY1tmYWNpbGl0aWVzXVxuZmMgLS0gam9pbiBieSBmYWNpbGl0eSAtLT4gbWRcbmRzIC0tIGpvaW4gdG8gZGlzdHJpY3QgLS0-IG5wYVthZGZdXG5hZFtBSFBDIHJlZ2lzdHJ5LCBhaHBjMjAxOF0gLS0-IG5wYVthZGZdXG5tZGFkZlttZGFfZGZdIC0tPiBmaW5hbFthZGZdXG5ucGFkZltucGFfZGZdIC0tPiBmaW5hbFxuZmluYWwgLS0-IHZmaW5hbFthZGZdXG52ZmluYWwgLS0-IHZhcnNcbnZhcnNbTWlzYyB2YXJzXSAtLT4gbW9kZWxbUnVuIG1vZGVsXVxuaHJoaXNbSFJJUywgaHJoaXMyMDE3XSAgLS0-IHZhY1tWYWNhbmNpZXMgZGYsIHVzZWQgYnkgdmFyIG5iXVxuZHMgLS0gam9pbiB0byBkaXN0cmljdCAtLT4gdmFjXG5zdWJncmFwaCBTb3VyY2VzXG4gICAgYWRcbiAgICBmbVxuICAgIHVtXG4gICAgYmdcbiAgICBocmhpc1xuZW5kXG5zdWJncmFwaCBGYWNpbGl0aWVzIG5vdGVib29rXG4gICAgZHNcbiAgICBmY1xuICAgdmFjXG5lbmRcbnN1YmdyYXBoIFBoeXNpY2lhbiBuYlxuICAgIG1kXG5lbmRcbnN1YmdyYXBoIE5QQSBuYlxuICAgIG5wYVxuZW5kXG5zdWJncmFwaCBXb3JrZm9yY2UgbmJcbiAgICBucGFkZlxuICAgIG1kYWRmXG4gICAgZmluYWxcbmVuZFxuc3ViZ3JhcGggVmFyaWFibGVzIG5iLCBwcm9jZXNzaW5nXG4gIHZmaW5hbFxuICB2YXJzXG5lbmRcbnN1YmdyYXBoIE1vZGVsIG5iXG4gIG1vZGVsXG5lbmQiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9fQ)



## Data flow within model 

The following diagram describes the flow of data currently used in the model as of Apr 5, 2018 3:15 PM. 

![data structure](../misc/data-flow.svg)

[Edit this diagram](https://mermaidjs.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcbmRzW2Rpc3RyaWN0c10gLS0-IGZjXG5iZ1tCdWRnZXQgb2ZmaWNlIGRpc3RyaWN0IGRhdGEsIG90aW1zXzIwMThdIC0tPiBkc1xudW1bVU1EUEMgcmVnaXN0cnksIHVtZHBjMjAxOF0gLS0-IG1kW2FkZl0gXG5tZCAtLT4gIG1kYWRmW21kYV9kZl1cbm5wYSAtLT4gbnBhZGZbbnBhX2RmXVxuZm1bRmFjaWxpdHkgbWFzdGVyIGxpc3QsIG1vaGRoaTIwMTddIC0tPiBmY1tmYWNpbGl0aWVzXVxuZmMgLS0gam9pbiBieSBmYWNpbGl0eSAtLT4gbWRcbmRzIC0tIGpvaW4gdG8gZGlzdHJpY3QgLS0-IG5wYVthZGZdXG5hZFtBSFBDIHJlZ2lzdHJ5LCBhaHBjMjAxOF0gLS0-IG5wYVthZGZdXG5tZGFkZlttZGFfZGZdIC0tPiBmaW5hbFthZGZdXG5ucGFkZltucGFfZGZdIC0tPiBmaW5hbFxuZmluYWwgLS0-IHZmaW5hbFthZGZdXG52ZmluYWwgLS0-IHZhcnNcbnZhcnNbTWlzYyB2YXJzXSAtLT4gbW9kZWxbUnVuIG1vZGVsXVxuaHJoaXNbSFJJUywgaHJoaXMyMDE3XSAgLS0-IHZhY1tWYWNhbmNpZXMgZGYsIHVzZWQgYnkgdmFyIG5iXVxuZHMgLS0gam9pbiB0byBkaXN0cmljdCAtLT4gdmFjXG5zdWJncmFwaCBTb3VyY2VzXG4gICAgYWRcbiAgICBmbVxuICAgIHVtXG4gICAgYmdcbiAgICBocmhpc1xuZW5kXG5zdWJncmFwaCBGYWNpbGl0aWVzIG5vdGVib29rXG4gICAgZHNcbiAgICBmY1xuICAgdmFjXG5lbmRcbnN1YmdyYXBoIFBoeXNpY2lhbiBuYlxuICAgIG1kXG5lbmRcbnN1YmdyYXBoIE5QQSBuYlxuICAgIG5wYVxuZW5kXG5zdWJncmFwaCBXb3JrZm9yY2UgbmJcbiAgICBucGFkZlxuICAgIG1kYWRmXG4gICAgZmluYWxcbmVuZFxuc3ViZ3JhcGggVmFyaWFibGVzIG5iLCBwcm9jZXNzaW5nXG4gIHZmaW5hbFxuICB2YXJzXG5lbmRcbnN1YmdyYXBoIE1vZGVsIG5iXG4gIG1vZGVsXG5lbmQiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9fQ)




## folder structure






## reference system
- overleaf.com
- https://latextools.readthedocs.io/en/latest/completions/


## Team / Collaborators (preliminary, unordered)
- Andrew Kintu, Association of Anesthesiologists of Uganda and Makerere University
- Fred Bulamba, Association of Anesthesiologists of Uganda, WFSA-ARS and Busitema University
- Tyler Law, UCSF
- Michael Lipnick, UCSF
- Alex Goodell, UCSF and Stanford alexgoodell@gmail.com
- Adam Hewitt Smith, Association of Anaesthetists of Great Britain and Ireland
- Stephen Ttendo, Association of Anesthesiologists of Uganda, Mbarara Regional Referral Hospital
- Maytinee Lilaonitkul, UCSF

