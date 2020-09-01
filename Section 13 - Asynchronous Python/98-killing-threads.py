# Don't kill threads
# If your thread has acquired the GIL, and you kill the thread manually, that thread could still have hold of the GIL and no other thread would be able to use it.
# This is called a deadlock
# If you kill threads, you'll have problems
