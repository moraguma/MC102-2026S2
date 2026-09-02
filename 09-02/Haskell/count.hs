main = loop 1
  where
    loop i
      | i <= 10 = do
        print i
        loop (i + 1)
      | otherwise = return ()