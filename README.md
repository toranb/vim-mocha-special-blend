# vim-mocha-special-blend

Ever want to run a single mocha test or module without having to find/replace?

## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/toranb/vim-mocha-special-blend ~/.vim/bundle/vim-mocha-special-blend`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Plugin 'toranb/vim-mocha-special-blend'` to .vimrc
  - Run `:PluginInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/toranb/vim-mocha-special-blend'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/toranb/vim-mocha-special-blend'` to .vimrc
  - Run `:PlugInstall`

## Requirements

You need a VIM version that was compiled with python support, which is typical
for most distributions on Linux/Mac.  You can check this by running
``vim --version | grep +python``
if you get a hit you are in business.

Tests are ran with either django-nose or nosetest so these will need to be
pip installed in order for the plugin to function properly.

## Usage

The plugin provides two commands:

```
    RunSingleMochaTest
    RunSingleMochaModule
```

All arguments can be tab-completed. Ensure that your cursor is within a
module or function as appropriate for the command being called.

For ease of usage you can map the above actions to a shortcut. For example,
if you wanted leader mappings you could set something like the following in
your vimrc:

```
    nmap <Leader>tm :call InvokeTestMethodByType()<CR>
    function! InvokeTestMethodByType()
        let action="npm test"
        exe ':RunSingleMochaTest ' . action
    endfunction

    nmap <Leader>tc :call InvokeTestClassByType()<CR>
    function! InvokeTestClassByType()
        let action="npm test"
        exe ':RunSingleMochaModule ' . action
    endfunction
```

## Credits

Most of the code used to write this plugin was stolen from the great Jarrod Taylor

https://github.com/JarrodCTaylor/vim-qunit-special-blend
