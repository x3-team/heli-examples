/**
 * Пользовательская функция для Google Таблиц: запрос к Heli (OpenAI-совместимый API).
 * Ключ HELI_API_KEY храните только в свойствах скрипта, не в коде и не в ячейках.
 *
 * @param {string} prompt Текст запроса к модели.
 * @param {string} [model] Необязательный слаг модели (по умолчанию openai/gpt-4.1-mini).
 * @return {string} Текст ответа ассистента или сообщение об ошибке.
 * @customfunction
 */
function ASK(prompt, model) {
  if (prompt === null || prompt === undefined || String(prompt).trim() === '') {
    return 'Укажите текст запроса: =ASK("ваш вопрос")';
  }

  var apiKey = PropertiesService.getScriptProperties().getProperty('HELI_API_KEY');
  if (!apiKey) {
    return 'Не задан HELI_API_KEY. Проект → Настройки проекта → Свойства скрипта.';
  }

  var modelName =
    model !== null && model !== undefined && String(model).trim() !== ''
      ? String(model)
      : 'openai/gpt-4.1-mini';

  var options = {
    method: 'post',
    contentType: 'application/json',
    headers: {
      Authorization: 'Bearer ' + apiKey,
    },
    payload: JSON.stringify({
      model: modelName,
      messages: [{ role: 'user', content: String(prompt) }],
    }),
    muteHttpExceptions: true,
  };

  var response = UrlFetchApp.fetch('https://getheli.ru/v1/chat/completions', options);
  var status = response.getResponseCode();
  var body = response.getContentText();

  if (status !== 200) {
    try {
      var errJson = JSON.parse(body);
      var errMsg =
        errJson.error && errJson.error.message ? errJson.error.message : body;
      return 'Heli HTTP ' + status + ': ' + errMsg;
    } catch (parseErr) {
      return 'Heli HTTP ' + status + ': ' + body;
    }
  }

  var data = JSON.parse(body);
  if (
    data.choices &&
    data.choices.length > 0 &&
    data.choices[0].message &&
    data.choices[0].message.content != null
  ) {
    return data.choices[0].message.content;
  }

  return 'Ответ API без текста в choices[0].message.content';
}
