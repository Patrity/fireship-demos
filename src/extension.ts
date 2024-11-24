import * as vscode from 'vscode'

const textToReplace = 'fireship'

export function activate(context: vscode.ExtensionContext) {
	let fireshipReplacer = vscode.workspace.onDidChangeTextDocument((event) => {
		const editor = vscode.window.activeTextEditor
		if (!editor) return

		const changes = event.contentChanges

		if (changes.length > 0) {
			const line = editor.document.lineAt(changes[0].range.start.line)
			const lineText = line.text

			const matches = [...lineText.matchAll(/fireship/g)]
			if (matches.length > 0) {
				const lastMatch = matches[matches.length - 1]
				const startPos = new vscode.Position(
					changes[0].range.start.line,
					lastMatch.index!
				)
                const endPos = new vscode.Position(
                    changes[0].range.start.line,
                    lastMatch.index! + textToReplace.length
                )

				editor.edit(editorBuilder => {
					editorBuilder.replace(new vscode.Range(startPos, endPos), '🔥')
				})
			}
		}
	})

	context.subscriptions.push(fireshipReplacer)

}