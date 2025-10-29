// Barrel exports for $lib consumers
export * from './assets';
// Centralized asset exports so components can import from `$lib/assets`
// Each variable holds the Vite-resolved URL string for the static file

import check from './assets/check.png';
import copy from './assets/copy.png';
import darkmode from './assets/darkmode.png';
import darkBg from './assets/dark_bg.png';
import editor from './assets/editor.png';
import errorIcon from './assets/error.png';
import errors from './assets/errors.png';
import favicon from './assets/favicon.svg';
import lightmode from './assets/lightmode.png';
import logo from './assets/logo.png';
import newFile from './assets/new_file.png';
import openFile from './assets/open_file.png';
import refresh from './assets/refresh.png';
import saveFile from './assets/save_file.png';
import synSemLexIcon from './assets/SynSemLexIcon.png';
import table from './assets/table.png';
import warning from './assets/warning.png';

export {
    check,
    copy,
    darkmode,
    darkBg,
    editor,
    errorIcon,
    errors,
    favicon,
    lightmode,
    logo,
    newFile,
    openFile,
    refresh,
    saveFile,
    synSemLexIcon,
    table,
    warning
};

// Aggregate object if you prefer programmatic access
export const assets = {
    check,
    copy,
    darkmode,
    darkBg,
    editor,
    errorIcon,
    errors,
    favicon,
    lightmode,
    logo,
    newFile,
    openFile,
    refresh,
    saveFile,
    synSemLexIcon,
    table,
    warning
};
