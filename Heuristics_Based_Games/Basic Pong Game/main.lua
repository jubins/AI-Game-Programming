function love.load()

	love.window.setMode(800,800)

	p1x = 0
	p1y = 400
	p1width = 10
	p1height = 100
	p1score = 0

	p2x = 800
	p2y = 400
	p2width = 10
	p2height = 100
	p2score = 0

	ballx = 400
	bally = 400
	ballxv = 5
	ballyv = 3
	balldiameter = 8

end

function love.update()

	treasurebox = love.graphics.newImage("treasurebox.png")

	ballx = ballx + ballxv
	bally = bally + ballyv
	
	if bally > 800 or bally < 0 then
		ballyv = -ballyv
	end

	if (ballx < p1x + p1width and bally > p1y and bally < p1y+p1height)
		or
		(ballx > p2x - p2width and bally > p2y and bally < p2y+p2height)
		then
		ballxv = - ballxv
	end

	if ballx > 800 then
		p1score = p1score + 1
		ballx = 400
		bally = 400
	elseif ballx < 0 then
		p2score = p2score + 1
		ballx = 400
		bally = 400
	end

	if love.keyboard.isDown("w") and p1y > 0 then
		p1y = p1y - 5
	elseif love.keyboard.isDown("s") and p1y + p1height < 800 then
		p1y = p1y + 5
	end

	if love.keyboard.isDown("up") and p2y > 0 then
		p2y = p2y - 5
	elseif love.keyboard.isDown("down") and p2y + p2height < 800 then
		p2y = p2y + 5
	end

end


function love.draw()

	love.graphics.draw(treasurebox, 200, 200)

	love.graphics.rectangle("fill", p1x, p1y, p1width, p1height)
	love.graphics.rectangle("fill", p2x, p2y, -p2width, p2height)

	love.graphics.rectangle("fill", ballx-balldiameter/2, bally-balldiameter/2, balldiameter, balldiameter)

	love.graphics.setNewFont(20)
	love.graphics.print(p1score, 380, 400)
	love.graphics.print(p2score, 420, 400)

end