Want to join the 40,000+ extensions in the VS Code marketplace? Let's build a completely useless (but educational) extension in the next few minutes.
 

## What are we building? 
A VS Code extension that replaces the word "fireship" with a fire emoji (🔥) as you type. Is it practical? No. Will it teach you the fundamentals of VS Code extension development? Absolutely.

  
## Project Setup
First, you'll need to set up your development environment. Use your favorite package manager to install the VS Code Extension Generator:

  
```bash
# Using pnpm
pnpm i --global yo generator-code

# Or using npx for one-time use
pnpm dlx --package yo --package generator-code -- yo code
```


## Your First Extension - Hi Mom!
The generator creates a basic "Hello World" extension. Let's modify it to say hi to our moms instead (because every programmer's first duty is to make their mother proud).

```typescript
import * as vscode from 'vscode'

export function activate(context: vscode.ExtensionContext) {
	let disposable = vscode.commands.registerCommand('yourExtension.hiMom', () => {
		vscode.window.showInformationMessage('Hi Mom! 👋')
	})
	
	context.subscriptions.push(disposable)
}
```

Don't forget to update your `package.json`:

```json
{
  "contributes": {
      "commands": [{
          "command": "yourExtension.hiMom",
          "title": "Hi Mom!"
      }]
  }
}
```

Test it out:
1. Press F5 to launch the Extension Development Host
2. Open the Command Palette (Cmd+Shift+P / Ctrl+Shift+P)
3. Type "Hi Mom"
4. Watch your touching message appear!


## Building the Fireship Replacer
Now let's build something more interesting. Here's our extension that replaces "fireship" with 🔥:
```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    // Create a disposable for our text change listener
    let disposable = vscode.workspace.onDidChangeTextDocument((event) => {
        const editor = vscode.window.activeTextEditor;
        if (!editor || event.document !== editor.document) {
            return;
        }

        const changes = event.contentChanges;
        if (changes.length === 0) return;

        // Look at the first change
        const change = changes[0];
        
        // Find matches of "fireship" in the changed text
        const matches = [...change.text.matchAll(/fireship/g)];
        
        if (matches.length > 0) {
            // Get the last match (most recently typed)
            const lastMatch = matches[matches.length - 1];
            
            // Create position objects for the replacement
            const startPos = new vscode.Position(
                change.range.start.line,
                lastMatch.index!
            );
            const endPos = new vscode.Position(
                change.range.start.line,
                lastMatch.index! + 'fireship'.length
            );

            // Replace the text
            editor.edit(editBuilder => {
                editBuilder.replace(new vscode.Range(startPos, endPos), '🔥');
            });
        }
    });

    context.subscriptions.push(disposable);
}
```

Update your `package.json` to activate the extension for specific languages:
```json
{
    "activationEvents": [
        "onLanguage:javascript",
        "onLanguage:typescript"
    ]
}
```


## Publishing to the Marketplace
Ready to share your creation with the world? Here's how:
1. Create a Microsoft account and Azure organization (free) at dev.azure.com
2. Install the VS Code Extension CLI:
```bash
npm install -g @vscode/vsce
```

3. Update your `package.json` with required fields:
```json
{
    "publisher": "your-publisher-name",
    "repository": {
        "type": "git",
        "url": "https://github.com/username/repo.git"
    },
    "icon": "icon.png",
    "version": "0.0.1"
}
```

4. Create a Personal Access Token (PAT) in Azure DevOps with Marketplace (publish) scope
5. Package and publish by running:
```bash
vsce package
vsce publish
```


## Practical Applications
While our emoji replacer might not change the world, you can use these same concepts to build actually useful extensions:
- Auto-format team commit messages
- Convert between different code syntaxes on the fly
- Add custom diagnostic warnings for your codebase
- Create snippets for your framework/library
- Add custom UI elements to VS Code


## Resources
- [VS Code Extension API Documentation](https://code.visualstudio.com/api)
- [Extension Guidelines](https://code.visualstudio.com/api/references/extension-guidelines)
- [Publishing Extensions](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)

  
## Conclusion
Now you're ready to contribute to the VS Code extension ecosystem. Whether you build something useful or just add to the chaos is entirely up to you. I'm not your developer advocate!
Remember: with great power comes great responsibility... or whatever.

---


Like this content? Follow me here:
- [YouTube](https://youtube.com/c/fireship)
- [Twitter](https://twitter.com/fireship_dev)
- [GitHub](https://github.com/fireship-io)