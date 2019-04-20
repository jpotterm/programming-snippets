from sorl.thumbnail import get_thumbnail


thumb = get_thumbnail(model.image, '96x96', crop=model.image.background_position(96, 96))
