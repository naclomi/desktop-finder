# desktop-finder
A platform-agnostic shell script that prints a path to the current user's desktop directory relative to the terminal's working directory. Optionally, can print the desktop's absolute directory instead.

Useful in classroom settings where the instructor might ask students to "cd
~/Desktop", since depending on operating system and the presence of backup
tools like Microsoft OneDrive, the desktop folder _may_ be somewhere other
than that.

Instructors can instead have students run this command (or pipe it from curl,
with a suitable warning about security practices) and then `cd` into the
directory that is outputted.

## Usage

```
./find-desktop.sh [--abs]
```

Or, remotely (before asking students to run this command, have them look at
what it's doing!!):

```
curl -s https://raw.githubusercontent.com/naclomi/desktop-finder/refs/heads/main/find-desktop.sh | sh
```

## License

Copyright (c) 2024 Naomi Alterman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.