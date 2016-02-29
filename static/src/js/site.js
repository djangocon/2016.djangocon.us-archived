/* global window ace */
window.jQuery = window.$ = require('jquery');

const $ = window.$;

require('bootstrap');

const loadEditors = () => {
    const $editors = $('.modal-body textarea, #id_body, #id_comment, #id_message, #id_text, #id_abstract, #id_additional_notes, #id_content_override, #id_description, #id_biography');
    $editors.each((i, el) => {
      const editorId = `markdown-editor-${i}`;
      const reportDiv = $('<div>').attr('id', editorId);
      const setupEditor = (editor, textarea) => {
          const session = editor.getSession();
          editor.setTheme('ace/theme/tomorrow');
          editor.$blockScrolling = Infinity;
          editor.setOption('scrollPastEnd', true);
          session.setMode('ace/mode/markdown');
          session.setValue(textarea.val());
          session.setUseWrapMode(true);
          session.on('change', () => {
              textarea.val(session.getValue());
          });
          editor.renderer.setShowGutter(false);
          session.setTabSize(4);
          session.setUseSoftTabs(true);
      };
      const $formGroup = $(el).closest('.form-group');
      const $textarea = $formGroup.find('textarea');
      $formGroup.append(reportDiv);
      setupEditor(ace.edit(editorId), $textarea);
    });
};

$(() => {
    loadEditors();
});
