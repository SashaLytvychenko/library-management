.. _changelog:

Changelog
=========

`17.0.1.0.0`
----------------
### Added
- Added tests to verify core module functionality.
- Added `uk_UA` translation.
- Included demo data and tests to showcase module features.
- Added an ``index.html`` file with a module description.

### Structure
- Created complete module structure with essential files and dependencies.

### Features
- Implemented LibraryBook model to manage the intake and tracking of books in the library, including ISBN, status, location, and other book attributes.
- Enforced unique ISBN constraint and restricted record deletion to 'draft' status only.
- Added actions for updating book statuses (e.g., available, borrowed, lost) and creating loan records.
- Integrated automatic status change to "available" when books are returned.

### Improvements
- Optimized model field structure and annotations for improved readability and user support.