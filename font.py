from pyrogram import Client, filters
from pyrogram.types import Message
app = Client(
       "bot", 
       api_id='21364355', 
       api_hash="72f11aec1dd3e5764554d477341a3d0b", 
       bot_token="6337104990:AAFxTIVSr3BtFxWEossUWZRbQIY4Dac8J4U"
) 

ALPHABET = {'Ⓐ', 'Ⓑ', 'Ⓒ', 'Ⓓ', 'Ⓔ', 'Ⓕ', 'Ⓖ', 'Ⓗ', 'Ⓘ', 'Ⓙ', 'Ⓚ', 'Ⓛ', 'Ⓜ', 'Ⓝ', 'Ⓞ','Ⓟ', 'Ⓠ', 'Ⓡ', 'Ⓢ', 'Ⓣ','Ⓤ','Ⓥ', 'Ⓦ', 'Ⓧ', 'Ⓨ', 'Ⓩ', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⓪','🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', '🅚', '🅛', '🅜', '🅝', '🅞','🅟', '🅠', '🅡', '🅢', '🅣','🅤','🅥', '🅦', '🅧', '🅨', '🅩', '❶', '❷', '❸', '❹', '❺', '❻', '❼', '❽', '❾', '⓿','Ａ', 'Ｂ', 'Ｃ', 'Ｄ', 'Ｅ', 'Ｆ', 'Ｇ', 'Ｈ', 'Ｉ', 'Ｊ', 'Ｋ', 'Ｌ', 'Ｍ', 'Ｎ', 'Ｏ','Ｐ', 'Ｑ', 'Ｒ', 'Ｓ', 'Ｔ','Ｕ','Ｖ', 'Ｗ', 'Ｘ', 'Ｙ', 'Ｚ', '１', '２', '３', '４', '５', '６', '７', '８', '９', '０','𝐀', '𝐁', '𝐂', '𝐃', '𝐄', '𝐅', '𝐆', '𝐇', '𝐈', '𝐉', '𝐊', '𝐋', '𝐌', '𝐍', '𝐎','𝐏', '𝐐', '𝐑', '𝐒', '𝐓','𝐔','𝐕', '𝐖', '𝐗', '𝐘', '𝐙', '𝟏', '𝟐', '𝟑', '𝟒', '𝟓', '𝟔', '𝟕', '𝟖', '𝟗', '𝟎','𝕬', '𝕭', '𝕮', '𝕯', '𝕰', '𝕱', '𝕲', '𝕳', '𝕴', '𝕵', '𝕶', '𝕷', '𝕸', '𝕹', '𝕺','𝕻', '𝕼', '𝕽', '𝕾', '𝕿','𝖀','𝖁', '𝖂', '𝖃', '𝖄', '𝖅', '𝟏', '𝟐', '𝟑', '𝟒', '𝟓', '𝟔', '𝟕', '𝟖', '𝟗', '𝟎','𝑨', '𝑩', '𝑪', '𝑫', '𝑬', '𝑭', '𝑮', '𝑯', '𝑰', '𝑱', '𝑲', '𝑳', '𝑴', '𝑵', '𝑶','𝑷', '𝑸', '𝑹', '𝑺', '𝑻','𝑼','𝑽', '𝑾', '𝑿', '𝒀', '𝒁', '𝟏', '𝟐', '𝟑', '𝟒', '𝟓', '𝟔', '𝟕', '𝟖', '𝟗', '𝟎','𝓐', '𝓑', '𝓒', '𝓓', '𝓔', '𝓕', '𝓖', '𝓗', '𝓘', '𝓙', '𝓚', '𝓛', '𝓜', '𝓝', '𝓞','𝓟', '𝓠', '𝓡', '𝓢', '𝓣','𝓤','𝓥', '𝓦', '𝓧', '𝓨', '𝓩', '𝟏', '𝟐', '𝟑', '𝟒', '𝟓', '𝟔', '𝟕', '𝟖', '𝟗', '𝟎','𝒜', '𝐵', '𝒞', '𝒟', '𝐸', '𝐹', '𝒢', '𝐻', '𝐼', '𝒥', '𝒦', '𝐿', '𝑀', '𝒩', '𝒪','𝒫', '𝒬', '𝑅', '𝒮', '𝒯','𝒰','𝒱', '𝒲', '𝒳', '𝒴', '𝒵','𝔸', '𝔹', 'ℂ', '𝔻', '𝔼', '𝔽', '𝔾', 'ℍ', '𝕀', '𝕁', '𝕂', '𝕃', '𝕄', 'ℕ', '𝕆','ℙ', 'ℚ', 'ℝ', '𝕊', '𝕋','𝕌','𝕍', '𝕎', '𝕏', '𝕐', 'ℤ', '𝟙', '𝟚', '𝟛', '𝟜', '𝟝', '𝟞', '𝟟', '𝟠', '𝟡', '𝟘','𝙰', '𝙱', '𝙲', '𝙳', '𝙴', '𝙵', '𝙶', '𝙷', '𝙸', '𝙹', '𝙺', '𝙻', '𝙼', '𝙽', '𝙾','𝙿', '𝚀', '𝚁', '𝚂', '𝚃','𝚄','𝚅', '𝚆', '𝚇', '𝚈', '𝚉', '𝟷', '𝟸', '𝟹', '𝟺', '𝟻', '𝟼', '𝟽', '𝟾', '𝟿', '𝟶','𝗔', '𝗕', '𝗖', '𝗗', '𝗘', '𝗙', '𝗚', '𝗛', '𝗜', '𝗝', '𝗞', '𝗟', '𝗠', '𝗡', '𝗢','𝗣', '𝗤', '𝗥', '𝗦', '𝗧','𝗨','𝗩', '𝗪', '𝗫', '𝗬', '𝗭', '𝟭', '𝟮', '𝟯', '𝟰', '𝟱', '𝟲', '𝟳', '𝟴', '𝟵', '𝟬','𝘼', '𝘽', '𝘾', '𝘿', '𝙀', '𝙁', '𝙂', '𝙃', '𝙄', '𝙅', '𝙆', '𝙇', '𝙈', '𝙉', '𝙊','𝙋', '𝙌', '𝙍', '𝙎', '𝙏','𝙐','𝙑', '𝙒', '𝙓', '𝙔', '𝙕', '𝟭', '𝟮', '𝟯', '𝟰', '𝟱', '𝟲', '𝟳', '𝟴', '𝟵', '𝟬','𝘈', '𝘉', '𝘊', '𝘋', '𝘌', '𝘍', '𝘎', '𝘏', '𝘐', '𝘑', '𝘒', '𝘓', '𝘔', '𝘕', '𝘖','𝘗', '𝘘', '𝘙', '𝘚', '𝘛','𝘜','𝘝', '𝘞', '𝘟', '𝘠', '𝘡', '𝟣', '𝟤', '𝟥', '𝟦', '𝟧', '𝟨', '𝟩', '𝟪', '𝟫', '𝟢','🄰', '🄱', '🄲', '🄳', '🄴', '🄵', '🄶', '🄷', '🄸', '🄹', '🄺', '🄻', '🄼', '🄽', '🄾','🄿', '🅀', '🅁', '🅂', '🅃','🅄','🅅', '🅆', '🅇', '🅈', '🅉','🅰', '🅱', '🅲', '🅳', '🅴', '🅵', '🅶', '🅷', '🅸', '🅹', '🅺', '🅻', '🅼', '🅽', '🅾','🅿', '🆀', '🆁', '🆂', '🆃','🆄','🆅', '🆆', '🆇', '🆈', '🆉','🇦​', '🇧​', '🇨​', '🇩​', '🇪​', '🇫​', '🇬​', '🇭​', '🇮​', '🇯​', '🇰​', '🇱​', '🇲​', '🇳​', '🇴​','🇵​', '🇶​', '🇷​', '🇸​', '🇹​','🇺​','🇻​', '🇼​', '🇽​', '🇾​', '🇿​','𝔄', '𝔅', 'ℭ', '𝔇', '𝔈', '𝔉', '𝔊', 'ℌ', 'ℑ', '𝔍', '𝔎', '𝔏', '𝔐', '𝔑', '𝔒','𝔓', '𝔔', 'ℜ', '𝔖', '𝔗','𝔘','𝔙', '𝔚', '𝔛', '𝔜', 'ℨ','ₐ', 'ᵦ', '꜀', 'd', 'ₑ', 'f', '₉', 'ₕ', 'ᵢ', 'ⱼ', 'ₖ', 'ₗ', 'ₘ', 'ₙ', 'ₒ','ₚ', 'q', 'ᵣ', 'ₛ', 'ₜ','ᵤ','ᵥ', 'w', 'ₓ', 'ᵧ', '₂', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉', '₀','ል', 'ጌ', 'ር', 'ዕ', 'ቿ', 'ቻ', 'ኗ', 'ዘ', 'ጎ', 'ጋ', 'ጕ', 'ረ', 'ጠ', 'ክ', 'ዐ','የ', 'ዒ', 'ዪ', 'ነ', 'ፕ','ሁ','ሀ', 'ሠ', 'ሸ', 'ሃ', 'ጊ', '˦', 'Ϩ', 'Յ', 'Ϥ', 'Ƽ', 'δ', '𐒇', 'ϐ', 'ƍ', 'θ','ﾑ', '乃', 'c', 'd', '乇', 'ｷ', 'g', 'ん', 'ﾉ', 'ﾌ', 'ズ', 'ﾚ', 'ﾶ', '刀', 'o','ｱ', 'q', '尺', '丂', 'ｲ','u','√', 'w', 'ﾒ', 'ﾘ', '乙', '⥑', 'ջ', 'ჳ', 'ʮ', 'ҕ', 'ϭ', '⁊', 'ზ', '𝚐', '○', '⓵', '⓶', '⓷', '⓸', '⓹', '⓺', '⓻', '⓼', '⓽', , '𝗔', '𝗕', '𝗖', '𝗗', '𝗘', '𝗙', '𝗚', '𝗛', '𝗜', '𝗝', '𝗞', '𝗟', '𝗠', '𝗡', '𝗢', '𝗣', '𝗤', '𝗥', '𝗦', '𝗧', '𝗨', '𝗩', '𝗪', '𝗫', '𝗬', '𝗭', 'Ä̈', 'ß', 'Ç̧', 'Ð', 'È', '£', 'G', 'Ì', 'ñ', 'Ö', 'þ', 'Q', '§', '†', 'Ú', '×', 'Ɏ', 'α', 'Ⴆ', 'ƈ', 'ԃ', 'ҽ', 'ϝ', 'ɠ', 'ԋ', 'ι', 'ʝ', 'ƙ', 'ʅ', 'ɱ', 'ɳ', 'σ', 'ρ', 'ϙ', 'ɾ', 'ʂ', 'ƚ', 'υ', 'ʋ', 'ɯ', 'x', 'ყ', 'ȥ', '🅰', '🅱', '🅲', '🅳', '🅴', '🅵', '🅶', '🅷', '🅸', '🅹', '🅺', '🅻', '🅼', '🅽', '🅾', '🅿', '🆀', '🆁', '🆂', '🆃', '🆄', '🆅', '🆆', '🆇', '🆈', '🆉', 'Ꭿ', 'Ᏸ', 'Ꮸ', 'Ꭰ', 'Ꭼ', 'Ꮀ', 'Ꮆ', 'Ꮋ', 'Ꭸ', 'Ꮰ', 'Ꮶ', 'Ꮭ', 'Ꮇ', 'Ꮑ', 'Ꮎ', 'Ꮲ', 'Ꮕ', 'Ꮢ', 'Ꮥ', 'Ꮏ', 'Ꮼ', 'Ꮙ', 'Ꮿ', 'Ꮂ', 'Ꮍ', 'Ꮓ', '🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', '🅚', '🅛', '🅜', '🅝', '🅞', '🅟', '🅠', '🅡', '🅢', '🅣', '🅤', '🅥', '🅦', '🅧', '🅨', '🅩', '𝔄', '𝔅', 'ℭ', '𝔇', '𝔈', '𝔉', '𝔊', 'ℌ', 'ℑ', '𝔍', '𝔎', '𝔏', '𝔐', '𝔑', '𝔒', '𝔓', '𝔔', 'ℜ', '𝔖', '𝔗', '𝔘', '𝔙', '𝔚', '𝔛', '𝔜', 'ℨ', '𝔤', '𝔥', '𝔦', '𝔧', '𝔨', '𝔩', '𝔪', '𝔫', '𝔬', '𝔭', '𝔮', '𝔯', '𝔰', '𝔱', '𝔲', '𝔳', '𝔴', '𝔵', '𝔶', '𝔷','ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ', 'ⓕ', 'ⓖ', 'ⓗ', 'ⓘ', 'ⓙ', 'ⓚ', 'ⓛ', 'ⓜ', 'ⓝ', 'ⓞ', 'ⓟ', 'ⓠ', 'ⓡ', 'ⓢ', 'ⓣ', 'ⓤ', 'ⓥ', 'ⓦ', 'ⓧ', 'ⓨ', 'ⓩ', 'Ⓐ', 'Ⓑ', 'Ⓒ', 'Ⓓ', 'Ⓔ', 'Ⓕ', 'Ⓖ', 'Ⓗ', 'Ⓘ', 'Ⓙ', 'Ⓚ', 'Ⓛ', 'Ⓜ', 'Ⓝ', 'Ⓞ', 'Ⓟ', 'Ⓠ', 'Ⓡ', 'Ⓢ', 'Ⓣ', 'Ⓤ', 'Ⓥ', 'Ⓦ', 'Ⓧ', 'Ⓨ', 'Ⓩ', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ', 'ł', 'J', '₭', 'Ⱡ', '₥', '₦', 'Ø', '₱', 'Q', 'Ɽ', '₴', '₮', 'Ʉ', 'V', '₩', 'Ӿ', 'Ɏ', 'Ⱬ', '𝘈', '𝘉', '𝘊', '𝘋', '𝘌', '𝘍', '𝘎', '𝘏', '𝘐', '𝘑', '𝘒', '𝘓', '𝘔', '𝘕', '𝘖', '𝘗', '𝘘', '𝘙', '𝘚', '𝘛', '𝘜', '𝘝', '𝘞', '𝘟', '𝘠', '𝘡', '𝘢', '𝘣', '𝘤', '𝘥', '𝘦', '𝘧', '𝘨', '𝘩', '𝘪', '𝘫', '𝘬', '𝘭', '𝘮', '𝘯', '𝘰', '𝘱', '𝘲', '𝘳', '𝘴', '𝘵', '𝘶', '𝘷', '𝘸', '𝘹', '𝘺', '𝘻'}

def contains_font(text):
    # Check if the message contains non-ASCII characters (indicating it's a font)
    return not all(char in ALPHABET for char in text)

@app.on_message(filters.text) 
def fonts(_, message:Message):
    if contains_font(message.text):
        message.delete() 
           
app.run() 
