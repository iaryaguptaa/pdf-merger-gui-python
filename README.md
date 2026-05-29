# Desktop PDF Merger GUI (Python)

A fully functional desktop application built in Python that provides a Graphical User Interface (GUI) to manage, reorder, and merge multiple PDF documents into a single consolidated file.

This project shifts from standard terminal scripting to event-driven programming, exploring GUI layouts, window component binding, external library integration, and file I/O streams.


## Features & Technical Highlights

* Graphical Interface: Crafted using Python's native Tkinter library, featuring a clean control window layout with standalone functional framing.
* Interactive File Listbox: Integrated a dynamic listbox displaying loaded file paths, complete with dedicated controller features to select, clear, or remove single items from memory tracking.
* Dynamic Index Reordering: Implemented custom indexing algorithm logic within the Move Up and Move Down operations to handle list matrix element swapping smoothly at runtime.
* File Stream Automation: Integrates the PyPDF library (PdfWriter) to handle actual background binary operations, merging sequential stream segments without file corruption.
* System Native Dialogs: Utilizes system file dialog modules like askopenfilenames and asksaveasfilename to bridge smooth interactive OS exploration directly into the tool.
* Exception & Alert Handling: Wrapped operations inside try-except structures with messagebox alerts to catch user handling exceptions or empty processing arrays safely.


## How To Run Locally

1. Clone the Project:
git clone https://github.com/iaryaguptaa/pdf-merger-gui-python.git

2. Install Dependencies:
pip install pypdf

3. Navigate and Run:
cd pdf-merger-gui-python
python main.py

4. Use: Click "Add PDFs" to load files, select a file and use "Move Up/Down" to arrange the sequence, then click "Merge" to save your new consolidated PDF!


## Key Learnings
* Designing event-driven object-oriented programming (OOP) layouts by extending Tkinter structures.
* Manipulating active list array placements dynamically based on structural user selections.
* Interfacing external file processing wheels securely inside functional desktop app boundaries.
