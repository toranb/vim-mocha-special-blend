python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

python << endOfPython
import os
def command_to_run_tests():
    return "npm test"
endOfPython

function! RunSingleTest()
python << endOfPython

current_line_index = vim.current.window.cursor[0]
current_test_line_num = sb.get_line_num_of_current_test(current_line_index, vim.current.buffer)
if current_test_line_num >= 0:
    vim.command(':wundo /tmp/oldUndo')
    vim.command(':!{}'.format(command_to_run_tests()))
    if os.path.isfile('/tmp/oldUndo'):
        vim.command('silent rundo /tmp/oldUndo')
        os.remove('/tmp/oldUndo')
    vim.command('silent wall')
else:
    print("This doesn't look like a mocha test file.")

endOfPython
endfunction

command! RunSingleMochaTest call RunSingleTest()
