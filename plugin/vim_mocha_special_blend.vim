python import os
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

python << endOfPython
import vim_mocha_special_blend as sb
endOfPython

function! RunSingleModule(command)
python << endOfPython

command_to_run = vim.eval("a:command")
current_line_index = vim.current.window.cursor[0]
current_module_line_num = sb.get_line_num_of_current_module(current_line_index, vim.current.buffer)
if current_module_line_num >= 0:
    vim.command(':wundo /tmp/oldUndo')
    vim.current.buffer[current_module_line_num] = sb.sub_current_module_with_singleModule(current_module_line_num, vim.current.buffer)
    vim.command(':!{}'.format(command_to_run))
    vim.current.buffer[current_module_line_num] = sb.sub_singleModule_with_module(current_module_line_num, vim.current.buffer)
    if os.path.isfile('/tmp/oldUndo'):
        vim.command('silent rundo /tmp/oldUndo')
        os.remove('/tmp/oldUndo')
    vim.command('silent wall')
else:
    print("This doesn't look like a mocha test file.")

endOfPython
endfunction

function! RunSingleTest(command)
python << endOfPython

command_to_run = vim.eval("a:command")
current_line_index = vim.current.window.cursor[0]
current_test_line_num = sb.get_line_num_of_current_test(current_line_index, vim.current.buffer)
if current_test_line_num >= 0:
    vim.command(':wundo /tmp/oldUndo')
    vim.current.buffer[current_test_line_num] = sb.sub_current_test_with_singleTest(current_test_line_num, vim.current.buffer)
    vim.command(':!{}'.format(command_to_run))
    vim.current.buffer[current_test_line_num] = sb.sub_singleTest_with_test(current_test_line_num, vim.current.buffer)
    if os.path.isfile('/tmp/oldUndo'):
        vim.command('silent rundo /tmp/oldUndo')
        os.remove('/tmp/oldUndo')
    vim.command('silent wall')
else:
    print("This doesn't look like a mocha test file.")

endOfPython
endfunction

command! -nargs=1 RunSingleMochaTest call RunSingleTest(<f-args>)
command! -nargs=1 RunSingleMochaModule call RunSingleModule(<f-args>)
