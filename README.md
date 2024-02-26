# To reproduce the issue
```
$ bazel run //app:app 

```

xcb error:
```
INFO: Analyzed target //app:app (0 packages loaded, 0 targets configured).
INFO: Found 1 target...
Target //app:app up-to-date:
  bazel-bin/app/app
INFO: Elapsed time: 0.047s, Critical Path: 0.00s
INFO: 1 process: 1 internal.
INFO: Build completed successfully, 1 total action
INFO: Running command line: bazel-bin/app/app
[xcb] Unknown sequence number while appending request
[xcb] You called XInitThreads, this is not your fault
[xcb] Aborting, sorry about that.
python3: ../../src/xcb_io.c:157: append_pending_request: Assertion `!xcb_xlib_unknown_seq_number' failed.
Aborted (core dumped)
```

# Workaround

```
$ bazel run //app:app  --noenable_bzlmod
```